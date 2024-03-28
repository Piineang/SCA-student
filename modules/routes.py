from fastapi import FastAPI


def set_route(app: FastAPI):
    from modules.company.controller import router as company_router
    app.include_router(company_router)
    
