import pandas as pd
import json
from config import Config
from dataset import DATASET
from assistant import email_assistant_app
from evaluator import EmailEvaluator

def run_evaluation_pipeline():
    # 1. Init and validate configuration environments
    Config.validate()
    evaluator = EmailEvaluator()
    
    # Define our two comparative evaluation paths
    strategies = [
        {"name": "Strategy_A_GPT4o_Mini", "model": "gpt-4o-mini", "temp": 0.1},
        {"name": "Strategy_B_Legacy_GPT35", "model": "gpt-3.5-turbo", "temp": 0.7}
    ]
    
    all_results_records = []
    summary_metrics = {}

    print(f"🚀 Launching Parallel Strategy Evaluation Pipeline over {len(DATASET)} Test Scenarios...")

    for strategy in strategies:
        print(f"\n⚡ Processing configuration harness: {strategy['name']}...")
        strategy_records = []
        
        m1_cumulative = 0
        m2_cumulative = 0
        m3_cumulative = 0
        
        for item in DATASET:
            # Execute Generation using the LangGraph Runtime execution loop
            inputs = {
                "intent": item["intent"],
                "key_facts": item["key_facts"],
                "tone": item["tone"],
                "model_name": strategy["model"],
                "temperature": strategy["temp"]
            }
            
            output_state = email_assistant_app.invoke(inputs)
            gen_email = output_state["clean_email"]
            
            # Execute Evaluation Matrix Evaluation Engine
            metrics = evaluator.evaluate_all(
                intent=item["intent"],
                key_facts=item["key_facts"],
                target_tone=item["tone"],
                generated_email=gen_email,
                human_reference=item["human_reference"]
            )
            
            m1_cumulative += metrics["metric_1_fact_recall"]
            m2_cumulative += metrics["metric_2_tone_alignment"]
            m3_cumulative += metrics["metric_3_conciseness_format"]
            
            # Append full records tracking structure
            record = {
                "Strategy": strategy["name"],
                "Scenario_ID": item["id"],
                "Intent": item["intent"],
                "Requested_Tone": item["tone"],
                "Generated_Email": gen_email,
                "M1_Fact_Recall": metrics["metric_1_fact_recall"],
                "M1_Reasoning": metrics["metric_1_reasoning"],
                "M2_Tone_Alignment": metrics["metric_2_tone_alignment"],
                "M2_Reasoning": metrics["metric_2_reasoning"],
                "M3_Conciseness_Format": metrics["metric_3_conciseness_format"],
                "M3_Reasoning": metrics["metric_3_reasoning"]
            }
            strategy_records.append(record)
            all_results_records.append(record)
            
        # Calculate Averages
        total_scenarios = len(DATASET)
        summary_metrics[strategy["name"]] = {
            "Avg_Fact_Recall_M1": round(m1_cumulative / total_scenarios, 2),
            "Avg_Tone_Alignment_M2": round(m2_cumulative / total_scenarios, 2),
            "Avg_Conciseness_M3": round(m3_cumulative / total_scenarios, 2),
            "Overall_Composite_Score": round((m1_cumulative + m2_cumulative + m3_cumulative) / (total_scenarios * 3), 2)
        }

    # Save out Structured Metrics Output Matrix Reports
    df_raw = pd.DataFrame(all_results_records)
    df_raw.to_csv("evaluation_raw_data_output.csv", index=False)
    
    with open("evaluation_summary_report.json", "w") as f:
        json.dump(summary_metrics, f, indent=4)
        
    # Print high level terminal display metrics console reporting layout
    print("\n================ EVALUATION SUMMARY REPORT ================")
    print(json.dumps(summary_metrics, indent=4))
    print("===========================================================")
    print("✨ Execution Successful. Structured metrics files written out to project directory.")

if __name__ == "__main__":
    run_evaluation_pipeline()