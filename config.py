# Configurations for all the agents

# General config
base_llm_model = "gpt-4o"
reasoning_llm_model = "o1-mini"
embedding_model = "text-embedding-3-large"
vector_store_collection_name = "brand_analysis"
vector_store_directory = "./chroma_langchain_db"

# Researcher agent
MAX_LOOP_COUNT = 5 # defines how many loops researcher modifies the query before it gives up and move on

# Writer agent
# List of sections in the report
sections = [{"title": "Trends", "section": "Emerging and Ongoing Social Trends Related to the Brand"},
            {"title": "Sentiment Ratio", "section": "brand's sentiment ratio within the target audience"},
            {"title": "Hot Topics", "section": "most discussed topics about the brand"},
            {"title": "Audience Preferences", "section": "target audience preferences"},
            {"title": "Brand Competitors", "section": "Which brands are the audience comparing the brand with"},
            {"title": "Opportunities", "section": "Strategic Opportunities for the brand"},
            {"title": "Actionables", "section": "actionables for the brand"}]