chai_type="plain"
def front_desk():
    def kitchen():
        global chai_type
        chai_type="irnai"
    kitchen()

front_desk()
print("final global chai:", chai_type)