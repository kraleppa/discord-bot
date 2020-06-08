response = {
    "C#": "Java lepsza :wink:",
    "Java": "C# lepszy :wink:",
    "C": "Chuja ssie",
    "Erlang": "Elixir lepszy :wink:",
    "Elixir": "Erlang lepszy :wink:"
}


def analyze_message(message):
    word_list = message.split()
    for word in word_list:
        if word in response:
            return response.get(word)
    return None
