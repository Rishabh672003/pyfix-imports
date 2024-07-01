test_code = """
start = time.time()
a = np.array([1, 2, 3, 4])
b = os.getcwd()


c = random.randint(1, 3)

deq = deque()
a = dedent("121")
d = defaultdict(str)

a = mp.sqrt_mod(12, 2)

itt = itertools.accumulate([1, 2, 3, 4])

print(list(itt))

assert list(itt) == [1, 3, 6, 10]

Points = collections.namedtuple("Point", ["x", "y"])


def fname(a: Dict[int, List], b: Tuple[int], c: Optional[List]):
    pass


z = os.getcwd()

end = time.time()
print(end - start)
"""
