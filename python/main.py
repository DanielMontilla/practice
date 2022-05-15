from top_k_frequent import topKFrequent


def main():
    nums = [73, 5, 3, 1, 1, 1, 3, 1]
    k = 2

    res = topKFrequent(nums, k)

    print(res)


if __name__ == '__main__':
    main()
