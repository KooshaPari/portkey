"""Portkey - LLM Gateway abstractions for multi-provider support.

A library for building LLM-powered applications with consistent interfaces
across different providers (OpenAI, Anthropic, Ollama, etc.).

Architecture:
    - domain/     : Pure domain models (no external dependencies)
    - application/: Use cases and port interfaces
    - infrastructure/: Provider implementations

Example:
    >>> from portkey import LLMGateway, OpenAIProvider
    >>> gateway = LLMGateway(providers=[OpenAIProvider()])
    >>> response = gateway.complete("Hello, world!")
"""
from portkey.domain.models import Message, Response
from portkey.application.ports import LLMProvider

__version__ = "0.1.0"

__all__ = [
    "Message",
    "Response",
    "LLMProvider",
]
