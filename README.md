# brandAnalysis
Performs brand analysis using LLMs and LangGraph

# functionalities
initial input
- brand name

The data/input:
- social signals, trends related to the brand
- target audience insights

output:
- trends: social trends about the brand
- insights: audience behavior, preferences, sentiments (basically a summary of social signals). note: target audience may not only use your brand as their service
- recommendations: recommendations for the brand

vector database

# thoughts
- The workflow is probably the same for every brand. So, decision making mainly comes from the RAG data procured
- I think we are basically building an agentic analytics solution
- if I have to count frequency for some insights, then LLMs are not well-suited for it

social signals
- Likes
- Shares
- Views
- Comments
- Click-through rates (CTR) 
- Number of followers
- Brand mentions
- Influencer engagement

# breakdown
- web scraping: just query the API to get relevant data. Search is handled by the App instead of myself
- database: just store the results scraped from the website
- non-agentic data analysis:
    - identify key trends
    - summarize social signals
    - store research results in a vector database
- agentic part:
    - explore actionable opportunities

frontend:
- input a brand name, click generate, outputs the entire text-based analytics

restrain yourself from overengineering. overcomplicated AI agents means slow and unscalable deployment

hard part: the sheer volume of data makes prompt engineering inefficient. This is the main hard point about this assignment

# plan
- build a basic map-reduce summarization agent for trends and social signals. use a RAG flow to determine how much data is crawled
- build a chain of thought, reflection agent to generate recommendations
- store state into PGVector
- build a frontend
- bonus: integrate reddit API, and other search engines. build in more visualization in final report