'''
https://leetcode.com/problems/design-browser-history/
1472. Design Browser History

You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
'''


class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class BrowserHistory(object):
    def __init__(self, homepage):
        new_page = Node(homepage)
        self.head = self.now = new_page

    def visit(self, url):
        self.now.next = Node(value=url, prev=self.now)
        self.now = self.now.next
        return None

    def back(self, steps):
        for _ in range(steps):
            if self.now.prev:
                self.now = self.now.prev
        return self.now.value

    def forward(self, steps):
        for _ in range(steps):
            if self.now.next:
                self.now = self.now.next
        return self.now.value


browser_history = BrowserHistory("leetcode.com")
browser_history.visit("google.com")
browser_history.visit("facebook.com")
browser_history.visit("youtube.com")
print(browser_history.back(1))
print(browser_history.back(1))
print(browser_history.forward(1))
browser_history.visit("linkedin.com")
print(browser_history.forward(2))
print(browser_history.back(2))
print(browser_history.back(7))

