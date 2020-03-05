#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")

    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "a88ac2d3-4217-4bc9-8963-cd4b69ea5067")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "ea7bc1a9-3ec7-4e07-aa14-dd7eab7bd039")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://websightcpf.azurewebsites.net/qnamaker")
