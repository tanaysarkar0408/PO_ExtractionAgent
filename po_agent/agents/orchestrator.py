from .extractor import ExtractorAgent
from .validator import ValidatorAgent
from ..memory.session import InMemorySessionService
import uuid

class OrchestratorAgent:
    def __init__(self):
        self.extractor = ExtractorAgent()
        self.validator = ValidatorAgent()
        self.session_service = InMemorySessionService()

    def process_po(self, pdf_path: str) -> dict:
        session_id = str(uuid.uuid4())
        self.session_service.create_session(session_id)
        
        print(f"Starting processing for {pdf_path} (Session: {session_id})")
        self.session_service.add_history(session_id, f"Started processing {pdf_path}")

        # Step 1: Extract
        print("Agent: Extractor... working...")
        extraction_result = self.extractor.extract(pdf_path)
        if "error" in extraction_result:
            return {"status": "failed", "reason": extraction_result["error"]}
        
        self.session_service.update_context(session_id, "extraction_raw", extraction_result)
        
        # Step 2: Validate
        print("Agent: Validator... working...")
        validation_result = self.validator.validate(extraction_result)
        self.session_service.update_context(session_id, "validation_result", validation_result)

        # Final Result
        return {
            "session_id": session_id,
            "status": "success" if validation_result["is_valid"] else "validation_failed",
            "data": extraction_result,
            "validation_errors": validation_result["errors"]
        }
