def call_itself(count):
    print('call_itself called!', count)
    if count < 10:
        call_itself(count + 1)

call_itself(0)

