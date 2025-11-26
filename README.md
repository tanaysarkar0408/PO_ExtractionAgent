# PO Extraction Agent

This agent extracts Purchase Order (PO) details from PDF files using a multi-agent architecture powered by Google's Generative AI.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Environment Configuration**:
    - Copy `.env.example` to `.env`:
      ```bash
      cp .env.example .env
      ```
    - Edit `.env` and add your `GOOGLE_API_KEY`.
    - *Note: If no API key is provided, the agent runs in "Mock Mode" with sample data.*

## Usage

Run the agent by providing the path to a PDF file:

```bash
python -m po_agent.main --input path/to/your/po.pdf
```

### Example

1.  Generate a sample PDF:
    ```bash
    python generate_sample_pdf.py
    ```

2.  Run the agent on the sample:
    ```bash
    python -m po_agent.main --input sample_po.pdf
    ```

## Architecture

- **Orchestrator**: Manages the workflow and session.
- **Extractor**: Reads PDF and uses LLM (Gemini) to extract structured data.
- **Validator**: Checks for missing or invalid fields.
