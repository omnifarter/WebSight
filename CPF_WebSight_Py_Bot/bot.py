# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
from flask import Config

from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount



class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.
    def __init__(self):
        self.qna_maker = QnAMaker(
            QnAMakerEndpoint(
                knowledge_base_id="a88ac2d3-4217-4bc9-8963-cd4b69ea5067",
                endpoint_key="ea7bc1a9-3ec7-4e07-aa14-dd7eab7bd039",
                host="https://websightcpf.azurewebsites.net/qnamaker",
        )
    )

    async def on_message_activity(self, turn_context: TurnContext):
    # The actual call to the QnA Maker service.
        response = await self.qna_maker.get_answers(turn_context)
        if response and len(response) > 0:
            await turn_context.send_activity(MessageFactory.text(response[0].answer))
        else:
            await turn_context.send_activity("No QnA Maker answers were found.")

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")
