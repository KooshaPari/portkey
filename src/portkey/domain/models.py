"""Domain models for portkey.

These models are pure domain objects with no external dependencies,
following Hexagonal Architecture principles.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Literal


class Role(str, Enum):
    """Message role in a conversation."""
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


class Provider(str, Enum):
    """Supported LLM providers."""
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    OLLAMA = "ollama"
    AZURE = "azure"
    VERTEX = "vertex"


@dataclass
class Message:
    """A single message in a conversation.

    Attributes:
        role: Who is speaking (system, user, assistant)
        content: The message content
        name: Optional name for the speaker
        tool_calls: Optional tool call requests
    """
    role: Role | Literal["system", "user", "assistant", "tool"]
    content: str
    name: str | None = None
    tool_calls: list[ToolCall] = field(default_factory=list)


@dataclass
class ToolCall:
    """A tool call request from the model."""
    id: str
    name: str
    arguments: dict


@dataclass
class ToolDefinition:
    """Definition of a tool the model can call."""
    name: str
    description: str
    parameters: dict  # JSON Schema


@dataclass
class Response:
    """Response from an LLM completion.

    Attributes:
        content: The text content of the response
        model: Model that generated the response
        provider: Provider that handled the request
        usage: Token usage statistics
        finish_reason: Why generation stopped
    """
    content: str
    model: str
    provider: Provider
    usage: Usage | None = None
    finish_reason: str | None = None
    tool_calls: list[ToolCall] = field(default_factory=list)


@dataclass
class Usage:
    """Token usage statistics."""
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0


@dataclass
class CompletionRequest:
    """Request for a completion.

    Attributes:
        messages: Conversation history
        model: Model identifier
        temperature: Sampling temperature (0-2)
        max_tokens: Maximum tokens to generate
        tools: Optional tool definitions
    """
    messages: list[Message]
    model: str
    temperature: float = 0.7
    max_tokens: int | None = None
    tools: list[ToolDefinition] | None = None
    stream: bool = False


@dataclass
class EmbeddingRequest:
    """Request for embeddings."""
    texts: list[str]
    model: str = "text-embedding-3-small"
    provider: Provider = Provider.OPENAI
