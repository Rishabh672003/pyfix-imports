test_code = """
start = time.perf_counter()
a = np.array([1, 2, 3, 4])
b = os.getcwd()


c = random.randint(1, 3)

deq = deque()
a = dedent("121")
d = defaultdict(str)

a = mp.sqrt_mod(12, 2)

itt = accumulate([1, 2, 3, 4])
itertools.count()

print(list(itt))


Points = collections.namedtuple("Point", ["x", "y"])


def fname(a: Dict[int, List], b: Tuple[int], c: Optional[List]):
    pass


z = os.getcwd()

end = time.perf_counter()
print(end - start)
"""
