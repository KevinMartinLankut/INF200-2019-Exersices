import collections as c
import math as m

def letter_freq(text):
    text = text.lower()
    cnt = c.Counter()
    for symbol in text:
        cnt[symbol] += 1
    return cnt


def entropy(message):
    N = len(message) #number of letters
    n_i = letter_freq(message) #number of occurences of letter i
    p_i = n_i/N #frequency of letter in message

#For example, if we have the message “abaa”, then we have p_{97} = 3/4, p_{98} = 1/4, and p_i = 0 for all other i. Then
#H = - \left(\frac{3}{4} \log_2 \frac{3}{4} + \frac{1}{4} \log_2 \frac{3}{4} \right) \text{bit} \approx 0.81 \text{bit}.

if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))