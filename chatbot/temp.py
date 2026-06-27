query = "address"
from knowledge_base import knowledge
for topics in knowledge:
    for key in knowledge[topics]:
        for message in knowledge[topics][key]:
            # print(knowledge[topics][key][message])
            if type(knowledge[topics][key][message]) == list:
                if query in knowledge[topics][key][message]:
                     print(knowledge[topics][key]['answer'])