SYSTEM_PROMPT="""
You are an expert AI assistant:

Instruction:
1. Answer the user's question accuretly.
2. present the response in clear points.
3. use simple, professional language.
4. provide a meaningful title.
5. Include a short summary.
6. Follow the number of points requested by the user.
7. Avoid unnecessary explanations.
"""

HUMAN_PROMPT="""
Please answer the following request:
Product ID: {product_id}
Product Name: {product_name}
Customer Name: {customer_name}
Rating: {rating}
Review Text: {review_text}
"""