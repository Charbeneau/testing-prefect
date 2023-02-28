from prefect import flow


@flow
def my_favorite_flow():
    return 42


if __name__ == "__main__":
    o = my_favorite_flow()
    print(o)
