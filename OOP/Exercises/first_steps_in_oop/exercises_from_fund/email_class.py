class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

output_list = []
command = input()
while command != "Stop":
    sender, receiver, content = command.split()
    output_list.append(Email(sender, receiver, content))
    command = input()
indexes = [int(index) for index in input().split(', ')]
for index in indexes:
    output_list[index].send()
for list in output_list:
    print(list.get_info())
