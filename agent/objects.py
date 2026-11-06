from pydantic import BaseModel , Field

class Answer(BaseModel):
    answer : str = Field(description="The answer that is needed for the user question")
    conversation : bool = Field(description="This is an indicator to know that conversation should still continue or not" \
            "if the agent agent has made the decision about the refund this should be False" \
            "if the conversation still needs more talk than its True" , default= True)


class PurchaseItem(BaseModel):
    name : str = Field(description="Name of the item purchased")
    