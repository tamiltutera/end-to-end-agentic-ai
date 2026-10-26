from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

# res = search_flights("Plan a 5 days itenary trips to switzerland")
# print(res)

# result = tavily_search("Best hotels in India", limit=5)
# print(result)

user_input = input("Enter travel request: ")
res = run_travel_agent(
    user_input = user_input,
    thread_id="test_user"
)
print("\n Final Response:\n")
print(res['answer'])

def main():
    # user_input = input("Enter travel request: ")
    user_input = "Can you plan my trip to Switzerland from Dhaka?"
    res = run_travel_agent(
        user_input = user_input,
        thread_id="test_user"
    )
    print("\n Final Response:\n")
    print(res['answer'])

if __name__ == "__main__":
    main()