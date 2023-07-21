def pi_name(aiger):
    def fn(i):
        return (
            aiger.get_name_by_id(i).decode("utf-8") if i in aiger._id_to_name else None
        )

    return fn
