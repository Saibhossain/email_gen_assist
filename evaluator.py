import json
import re
from typing import Dict, Any
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from prompts import TONE_EVAL_PROMPT, FACT_HAL_EVAL_PROMPT

class EmailEvaluator:
    def __init__(self):
        # Using a reliable judge LLM for metric tracking
        self.judge_llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

    def evaluate_all(self, intent: str, key_facts: str, target_tone: str, generated_email: str, human_reference: str) -> Dict[str, Any]:
        """ Executes our three custom designed evaluation metrics """
        
        # Metric 1: Programmatic Fact Recall & Hallucination Assessment via LLM Judge
        metric_1_data = self._calculate_fact_recall(key_facts, generated_email)
        
        # Metric 2: LLM-as-a-Judge Tone Accuracy Alignment
        metric_2_data = self._calculate_tone_accuracy(target_tone, generated_email)
        
        # Metric 3: Structural Conciseness & Format Adherence (Hybrid metric)
        metric_3_data = self._calculate_structural_conciseness(generated_email, human_reference)
        
        return {
            "metric_1_fact_recall": metric_1_data["score"],
            "metric_1_reasoning": metric_1_data["reasoning"],
            "metric_2_tone_alignment": metric_2_data["score"],
            "metric_2_reasoning": metric_2_data["reasoning"],
            "metric_3_conciseness_format": metric_3_data["score"],
            "metric_3_reasoning": metric_3_data["reasoning"]
        }

    def _calculate_fact_recall(self, key_facts: str, generated_email: str) -> Dict[str, Any]:
        prompt = PromptTemplate.from_template(FACT_HAL_EVAL_PROMPT).format(
            key_facts=key_facts,
            generated_email=generated_email
        )
        try:
            res = self.judge_llm.invoke(prompt)
            return self._parse_json_markdown(res.content)
        except Exception as e:
            return {"score": 1, "reasoning": f"Parser failure: {str(e)}"}

    def _calculate_tone_accuracy(self, target_tone: str, generated_email: str) -> Dict[str, Any]:
        prompt = PromptTemplate.from_template(TONE_EVAL_PROMPT).format(
            target_tone=target_tone,
            generated_email=generated_email
        )
        try:
            res = self.judge_llm.invoke(prompt)
            return self._parse_json_markdown(res.content)
        except Exception as e:
            return {"score": 1, "reasoning": f"Parser failure: {str(e)}"}

    def _calculate_structural_conciseness(self, generated_email: str, human_reference: str) -> Dict[str, Any]:
        """
        Custom Metric 3 (Hybrid Formulaic): Checks basic email syntax blocks (Subject/Body),
        and applies structural length variance constraints against the human standard baseline.
        """
        score = 5
        reasons = []
        
        # Checklist 1: Standard professional components presence
        has_subject = bool(re.search(r'(?i)subject:', generated_email))
        if not has_subject:
            score -= 1.5
            reasons.append("Missing explicit structural 'Subject:' header.")
            
        # Checklist 2: Check for excessive boilerplate vs human standard
        gen_word_count = len(generated_email.split())
        ref_word_count = len(human_reference.split())
        
        # If generated email word length is greater than double the human baseline reference, penalize density
        if gen_word_count > (ref_word_count * 1.6):
            score -= 1.5
            reasons.append(f"Fails Conciseness: Bloated word-density ({gen_word_count} words vs Ref {ref_word_count} words).")
        elif gen_word_count < (ref_word_count * 0.4):
            score -= 1.5
            reasons.append("Fails Structure: Too short to maintain standard opening/closing phrasing guidelines.")
            
        if score < 1: 
            score = 1.0
            
        return {
            "score": round(score, 1),
            "reasoning": " | ".join(reasons) if reasons else "Perfect architectural structure and semantic density balance."
        }

    def _parse_json_markdown(self, text: str) -> Dict[str, Any]:
        """ Secure parsing utility extracting clean JSON out of raw chat returns """
        try:
            clean_text = text.strip()
            if "```json" in clean_text:
                clean_text = clean_text.split("```json")[1].split("```")[0].strip()
            elif "```" in clean_text:
                clean_text = clean_text.split("```")[1].split("```")[0].strip()
            return json.loads(clean_text)
        except Exception:
            # Fallback regex lookups if structure breaks down
            score_match = re.search(r'"score":\s*(\d)', text)
            score = int(score_match.group(1)) if score_match else 3
            return {"score": score, "reasoning": "Fallback extraction executed."}