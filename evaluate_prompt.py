import json
import re
import os
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from config import Config
from dataset import DATASET
from prompts import EMAIL_GENERATION_SYSTEM_PROMPT

class PromptPerformanceEvaluator:
    def __init__(self, model_name: str = "gpt-4.1-nano-2025-04-14"):
        Config.validate()
        self.llm = ChatOpenAI(model=model_name, temperature=0.3)
        self.prompt_template = PromptTemplate.from_template(EMAIL_GENERATION_SYSTEM_PROMPT)

    def run_prompt_evaluation(self, output_json_path: str = "prompt_performance_report.json"):
        print(f"🔬 Evaluating Prompt Template Robustness over {len(DATASET)} test cases...")
        
        results = []
        adherence_count = 0
        leakage_free_count = 0
        total_efficiency_score = 0.0

        for item in DATASET:
            formatted_prompt = self.prompt_template.format(
                intent=item["intent"],
                key_facts=item["key_facts"],
                tone=item["tone"]
            )
            
            # Execute token length calculations for structural efficiency tracking
            prompt_tokens = len(formatted_prompt.split())
            
            # Invoke model execution
            response = self.llm.invoke(formatted_prompt)
            raw_output = response.content
            output_tokens = len(raw_output.split())

            # --- PROMPT METRIC 1: Instruction Adherence (Thinking Tags) ---
            # Verifies if the prompt successfully forced the model to generate <thinking> blocks
            has_thinking_tags = bool(re.search(r"<thinking>([\s\S]*?)</thinking>", raw_output))
            adherence_score = 1.0 if has_thinking_tags else 0.0
            if has_thinking_tags:
                adherence_count += 1

            # --- PROMPT METRIC 2: Context Isolation (Few-Shot Leakage) ---
            # Checks if entities from the few-shot examples ("Alex", "Sarah", "Lisbon") leaked into wrong inputs
            few_shot_entities = ["alex", "sarah", "lisbon", "apac"]
            lowered_output = raw_output.lower()
            
            # Filter entities that actually belong to the current scenario's context
            current_context = (item["intent"] + " " + item["key_facts"]).lower()
            leaked_entities = []
            
            for entity in few_shot_entities:
                if entity in lowered_output and entity not in current_context:
                    leaked_entities.append(entity)
            
            leakage_score = 1.0 if len(leaked_entities) == 0 else 0.0
            if leakage_score == 1.0:
                leakage_free_count += 1

            # --- PROMPT METRIC 3: Prompt Efficiency Ratio ---
            # Measures if the template is overly verbose or optimally driving text generation density
            efficiency_ratio = round(output_tokens / prompt_tokens, 3)
            total_efficiency_score += efficiency_ratio

            results.append({
                "scenario_id": item["id"],
                "metrics": {
                    "instruction_adherence_passed": has_thinking_tags,
                    "few_shot_leakage_detected": len(leaked_entities) > 0,
                    "leaked_entities": leaked_entities,
                    "token_efficiency_ratio": efficiency_ratio
                }
            })

        # Aggregate summary metrics for the prompt architecture
        total_cases = len(DATASET)
        prompt_performance_summary = {
            "prompt_metadata": {
                "template_char_length": len(EMAIL_GENERATION_SYSTEM_PROMPT),
                "total_test_scenarios_evaluated": total_cases
            },
            "aggregated_scores": {
                "instruction_adherence_rate": round(adherence_count / total_cases, 2),
                "context_isolation_rate": round(leakage_free_count / total_cases, 2),
                "average_generation_efficiency_ratio": round(total_efficiency_score / total_cases, 2)
            },
            "per_scenario_breakdown": results
        }

        # Write output results strictly to structured JSON format
        with open(output_json_path, "w") as json_file:
            json.dump(prompt_performance_summary, json_file, indent=4)

        print(f"Prompt evaluation complete! Scores saved directly to: '{output_json_path}'")
        return prompt_performance_summary

if __name__ == "__main__":
    evaluator = PromptPerformanceEvaluator()
    evaluator.run_prompt_evaluation()