import os
from app.core.hubscape_adk import get_context, require_tool_privilege

@require_tool_privilege
async def show_org_details_form() -> dict:
    """
    Renders the organization details form widget to the user to collect organization onboarding details.
    """
    ctx = get_context()
    ctx.show_widget("org_details_form")
    return {
        "status": "success",
        "message": "Organization details form widget successfully rendered."
    }
