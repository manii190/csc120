def post_order(bt):
    if bt is None:
        return
    else:
        post_order(bt.left())
        post_order(bt.right())
        print(bt.value())