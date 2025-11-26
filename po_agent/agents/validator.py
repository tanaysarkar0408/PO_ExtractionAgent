class ValidatorAgent:
    def validate(self, data: dict) -> dict:
        """
        Validates the extracted PO data.
        """
        errors = []
        if not data.get("po_number"):
            errors.append("Missing PO Number")
        if not data.get("po_date"):
            errors.append("Missing PO Date")
        if not data.get("customer_name"):
            errors.append("Missing Customer Name")
        
        items = data.get("items", [])
        if not items:
            errors.append("No items found")
        else:
            for i, item in enumerate(items):
                if not item.get("code"):
                    errors.append(f"Item {i+1} missing code")
                if not item.get("quantity"):
                    errors.append(f"Item {i+1} missing quantity")

        return {
            "is_valid": len(errors) == 0,
            "errors": errors,
            "data": data
        }
