class Counter:
    count = 0

    # modifica clase o objeto, el parametro cls es la clase
    @classmethod
    def increment(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

Counter.increment()
Counter.increment()
print(Counter.get_count())  # Output: 2