#!/usr/bin/python3
def magic_string(container={"counter": 0}):
    container["counter"] += 1
    return (", ".join(["BestSchool"] * (container["counter"])))
