import asyncio

from agents import Runner
from agents.testing import ScriptedModel
from agents.testing.model import ModelStep, ResponseOutputMessage, ResponseOutputText

from projeto_ia.agent import agent


def test_agent_returns_scripted_response():
    model = ScriptedModel(
        steps=[
            ModelStep(
                output=[
                    ResponseOutputMessage(
                        id="msg-1",
                        content=[
                            ResponseOutputText(
                                annotations=[],
                                text="Resposta de teste",
                                type="output_text",
                            )
                        ],
                        role="assistant",
                        status="completed",
                        type="message",
                    )
                ]
            )
        ]
    )

    test_agent = agent.clone(model=model)
    result = asyncio.run(Runner.run(test_agent, "Olá"))

    assert result.final_output == "Resposta de teste"
