# правильное начало — разведка данных
def profile_dataset(records: list[dict]) -> dict:
    if not records:
        return {}
    keys = records[0].keys()
    profile = {}
    for key in keys:
        values = [r[key] for r in records]
        profile[key] = {
            "total": len(values),
            "missing": sum(1 for v in values if v is None or v == ""),
            "unique": len(set(v for v in values if v is not None)),
            "sample": values[:3],
        }
    return profile
