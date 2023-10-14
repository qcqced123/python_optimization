def function(args) -> None:
    args += ' in runtime'
    print(args)


mutable = list('mutable')
function(mutable)
print(mutable)
