import argparse
import os
import json
from dotenv import load_dotenv
from po_agent.agents.orchestrator import OrchestratorAgent

def main():
    load_dotenv()
    
    parser = argparse.ArgumentParser(description="PO Extraction Agent")
    parser.add_argument("--input", required=True, help="Path to the PO PDF file")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: File {args.input} not found.")
        return

    agent = OrchestratorAgent()
    result = agent.process_po(args.input)
    
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
