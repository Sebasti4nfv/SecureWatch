from app.correlation import aplica_reglas

def test_reglas_sigma_detectan_incidente():
    logs = [{"user": "alice", "success": False} for x in range(6)]
    
    incidente = aplica_reglas(logs)
    
    assert incidente["tipo"] == "multiple_failed_logins"
    assert incidente["severidad"] == "high"