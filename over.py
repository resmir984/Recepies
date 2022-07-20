#self==>current instance,super==>for parent class calling
class Parent:

    def properties(self):
        self.props={"gold":"2kg","bike":"passionpro"}

        return self.props
class Child(Parent):
    def properties(self):
        props=super().properties()
        props["car"]="swift"
        #props={"car":"swift"}
        return self.props
ch=Child()
print(ch.properties())
