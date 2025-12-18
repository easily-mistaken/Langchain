from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
  "Lionel Messi is an Argentine footballer widely regarded as the GOAT, known for his extraordinary dribbling, vision, and goal-scoring ability.",
  "Cristiano Ronaldo is a Portuguese footballer famous for his athleticism, goal-scoring consistency, and elite mentality.",
  "Neymar Jr. is a Brazilian footballer known for his flair, creativity, and technical brilliance on the ball.",
  "Kylian Mbappé is a French footballer recognized for his explosive pace, finishing, and dominance at a young age.",
  "Kevin De Bruyne is a Belgian midfielder celebrated for his passing range, vision, and playmaking intelligence.",
  "Zinedine Zidane was a French football legend admired for his elegance, ball control, and big-game performances.",
  "Ronaldinho was a Brazilian football icon known for his joy, flair, and magical skills that entertained fans worldwide.",
  "Erling Haaland is a Norwegian striker known for his physicality, positioning, and incredible goal-scoring rate.",
  "Luka Modrić is a Croatian midfielder respected for his composure, passing accuracy, and control of the game’s tempo.",
  "Xavi Hernández is a Spanish footballer renowned for his positional intelligence and mastery of tiki-taka football.",
  "Andrés Iniesta is a Spanish football legend famous for his close control, creativity, and clutch performances.",
  "Sergio Ramos is a Spanish defender known for his leadership, aggression, and decisive goals in crucial moments.",
  "Manuel Neuer is a German goalkeeper credited with revolutionizing the sweeper-keeper role.",
  "Thierry Henry is a French football great celebrated for his pace, elegance, and lethal finishing.",
  "Paolo Maldini was an Italian defensive legend admired for his positioning, longevity, and leadership."
]

query = "Who is the GOAT of football?"

doc_embeddings = embedding.embed_documents(documents)
# print(str(doc_embeddings))

query_embedding = embedding.embed_query(query)
# print(str(query_embedding))

similarity_scores = cosine_similarity([query_embedding], doc_embeddings)[0]
# print(similarity_scores)

index, score = sorted(list(enumerate(similarity_scores)), key=lambda x: x[1], reverse=True)[0]

print("Query: " + query)
print("Most similar document: " + documents[index])
print("Similarity score: " + str(score))