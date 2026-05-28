from transformers import BertTokenizer, BertModel 
import torch
line1 = "I have to bank, my father gave money which i have to deposit"
line2 = "I like to do camp near bank of river"

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def get_contextual_embeddings(sentence):
    # print(sentence)
    input = tokenizer(sentence,return_tensors='pt')
    output = model(**input)
    tokens = tokenizer.convert_ids_to_tokens(input['input_ids'][0])
    position = tokens.index('bank')
    embedding = output.last_hidden_state[0][position]
    return embedding


result1 = get_contextual_embeddings(line1)
result2 = get_contextual_embeddings(line2)

temp = torch.cosine_similarity(result1.unsqueeze(0),result2.unsqueeze(0)).squeeze().item()
print(temp)



