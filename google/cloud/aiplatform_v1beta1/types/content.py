# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.cloud.aiplatform_v1beta1.types import tool
from google.protobuf import duration_pb2  # type: ignore
from google.type import date_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.aiplatform.v1beta1",
    manifest={
        "HarmCategory",
        "Content",
        "Part",
        "Blob",
        "FileData",
        "VideoMetadata",
        "GenerationConfig",
        "SafetySetting",
        "SafetyRating",
        "CitationMetadata",
        "Citation",
        "Candidate",
    },
)


class HarmCategory(proto.Enum):
    r"""Harm categories that will block the content.

    Values:
        HARM_CATEGORY_UNSPECIFIED (0):
            The harm category is unspecified.
        HARM_CATEGORY_HATE_SPEECH (1):
            The harm category is hate speech.
        HARM_CATEGORY_DANGEROUS_CONTENT (2):
            The harm category is dangerous content.
        HARM_CATEGORY_HARASSMENT (3):
            The harm category is harassment.
        HARM_CATEGORY_SEXUALLY_EXPLICIT (4):
            The harm category is sexually explicit
            content.
    """
    HARM_CATEGORY_UNSPECIFIED = 0
    HARM_CATEGORY_HATE_SPEECH = 1
    HARM_CATEGORY_DANGEROUS_CONTENT = 2
    HARM_CATEGORY_HARASSMENT = 3
    HARM_CATEGORY_SEXUALLY_EXPLICIT = 4


class Content(proto.Message):
    r"""The base structured datatype containing multi-part content of a
    message.

    A ``Content`` includes a ``role`` field designating the producer of
    the ``Content`` and a ``parts`` field containing multi-part data
    that contains the content of the message turn.

    Attributes:
        role (str):
            Optional. The producer of the content. Must
            be either 'user' or 'model'.
            Useful to set for multi-turn conversations,
            otherwise can be left blank or unset.
        parts (MutableSequence[google.cloud.aiplatform_v1beta1.types.Part]):
            Required. Ordered ``Parts`` that constitute a single
            message. Parts may have different IANA MIME types.
    """

    role: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parts: MutableSequence["Part"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Part",
    )


class Part(proto.Message):
    r"""A datatype containing media that is part of a multi-part ``Content``
    message.

    A ``Part`` consists of data which has an associated datatype. A
    ``Part`` can only contain one of the accepted types in
    ``Part.data``.

    A ``Part`` must have a fixed IANA MIME type identifying the type and
    subtype of the media if ``inline_data`` or ``file_data`` field is
    filled with raw bytes.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (str):
            Optional. Text part (can be code).

            This field is a member of `oneof`_ ``data``.
        inline_data (google.cloud.aiplatform_v1beta1.types.Blob):
            Optional. Inlined bytes data.

            This field is a member of `oneof`_ ``data``.
        file_data (google.cloud.aiplatform_v1beta1.types.FileData):
            Optional. URI based data.

            This field is a member of `oneof`_ ``data``.
        function_call (google.cloud.aiplatform_v1beta1.types.FunctionCall):
            Optional. A predicted [FunctionCall] returned from the model
            that contains a string representing the
            [FunctionDeclaration.name] with the parameters and their
            values.

            This field is a member of `oneof`_ ``data``.
        function_response (google.cloud.aiplatform_v1beta1.types.FunctionResponse):
            Optional. The result output of a [FunctionCall] that
            contains a string representing the
            [FunctionDeclaration.name] and a structured JSON object
            containing any output from the function call. It is used as
            context to the model.

            This field is a member of `oneof`_ ``data``.
        video_metadata (google.cloud.aiplatform_v1beta1.types.VideoMetadata):
            Optional. Video metadata. The metadata should only be
            specified while the video data is presented in inline_data
            or file_data.

            This field is a member of `oneof`_ ``metadata``.
    """

    text: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="data",
    )
    inline_data: "Blob" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="data",
        message="Blob",
    )
    file_data: "FileData" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="data",
        message="FileData",
    )
    function_call: tool.FunctionCall = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="data",
        message=tool.FunctionCall,
    )
    function_response: tool.FunctionResponse = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="data",
        message=tool.FunctionResponse,
    )
    video_metadata: "VideoMetadata" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="metadata",
        message="VideoMetadata",
    )


class Blob(proto.Message):
    r"""Raw media bytes.

    Text should not be sent as raw bytes, use the 'text' field.

    Attributes:
        mime_type (str):
            Required. The IANA standard MIME type of the
            source data.
        data (bytes):
            Required. Raw bytes for media formats.
    """

    mime_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )


class FileData(proto.Message):
    r"""URI based data.

    Attributes:
        mime_type (str):
            Required. The IANA standard MIME type of the
            source data.
        file_uri (str):
            Required. URI.
    """

    mime_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    file_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


class VideoMetadata(proto.Message):
    r"""Metadata describes the input video content.

    Attributes:
        start_offset (google.protobuf.duration_pb2.Duration):
            Optional. The start offset of the video.
        end_offset (google.protobuf.duration_pb2.Duration):
            Optional. The end offset of the video.
    """

    start_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    end_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )


class GenerationConfig(proto.Message):
    r"""Generation config.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        temperature (float):
            Optional. Controls the randomness of
            predictions.

            This field is a member of `oneof`_ ``_temperature``.
        top_p (float):
            Optional. If specified, nucleus sampling will
            be used.

            This field is a member of `oneof`_ ``_top_p``.
        top_k (float):
            Optional. If specified, top-k sampling will
            be used.

            This field is a member of `oneof`_ ``_top_k``.
        candidate_count (int):
            Optional. Number of candidates to generate.

            This field is a member of `oneof`_ ``_candidate_count``.
        max_output_tokens (int):
            Optional. The maximum number of output tokens
            to generate per message.

            This field is a member of `oneof`_ ``_max_output_tokens``.
        stop_sequences (MutableSequence[str]):
            Optional. Stop sequences.
    """

    temperature: float = proto.Field(
        proto.FLOAT,
        number=1,
        optional=True,
    )
    top_p: float = proto.Field(
        proto.FLOAT,
        number=2,
        optional=True,
    )
    top_k: float = proto.Field(
        proto.FLOAT,
        number=3,
        optional=True,
    )
    candidate_count: int = proto.Field(
        proto.INT32,
        number=4,
        optional=True,
    )
    max_output_tokens: int = proto.Field(
        proto.INT32,
        number=5,
        optional=True,
    )
    stop_sequences: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )


class SafetySetting(proto.Message):
    r"""Safety settings.

    Attributes:
        category (google.cloud.aiplatform_v1beta1.types.HarmCategory):
            Required. Harm category.
        threshold (google.cloud.aiplatform_v1beta1.types.SafetySetting.HarmBlockThreshold):
            Required. The harm block threshold.
    """

    class HarmBlockThreshold(proto.Enum):
        r"""Probability based thresholds levels for blocking.

        Values:
            HARM_BLOCK_THRESHOLD_UNSPECIFIED (0):
                Unspecified harm block threshold.
            BLOCK_LOW_AND_ABOVE (1):
                Block low threshold and above (i.e. block
                more).
            BLOCK_MEDIUM_AND_ABOVE (2):
                Block medium threshold and above.
            BLOCK_ONLY_HIGH (3):
                Block only high threshold (i.e. block less).
            BLOCK_NONE (4):
                Block none.
        """
        HARM_BLOCK_THRESHOLD_UNSPECIFIED = 0
        BLOCK_LOW_AND_ABOVE = 1
        BLOCK_MEDIUM_AND_ABOVE = 2
        BLOCK_ONLY_HIGH = 3
        BLOCK_NONE = 4

    category: "HarmCategory" = proto.Field(
        proto.ENUM,
        number=1,
        enum="HarmCategory",
    )
    threshold: HarmBlockThreshold = proto.Field(
        proto.ENUM,
        number=2,
        enum=HarmBlockThreshold,
    )


class SafetyRating(proto.Message):
    r"""Safety rating corresponding to the generated content.

    Attributes:
        category (google.cloud.aiplatform_v1beta1.types.HarmCategory):
            Output only. Harm category.
        probability (google.cloud.aiplatform_v1beta1.types.SafetyRating.HarmProbability):
            Output only. Harm probability levels in the
            content.
        blocked (bool):
            Output only. Indicates whether the content
            was filtered out because of this rating.
    """

    class HarmProbability(proto.Enum):
        r"""Harm probability levels in the content.

        Values:
            HARM_PROBABILITY_UNSPECIFIED (0):
                Harm probability unspecified.
            NEGLIGIBLE (1):
                Negligible level of harm.
            LOW (2):
                Low level of harm.
            MEDIUM (3):
                Medium level of harm.
            HIGH (4):
                High level of harm.
        """
        HARM_PROBABILITY_UNSPECIFIED = 0
        NEGLIGIBLE = 1
        LOW = 2
        MEDIUM = 3
        HIGH = 4

    category: "HarmCategory" = proto.Field(
        proto.ENUM,
        number=1,
        enum="HarmCategory",
    )
    probability: HarmProbability = proto.Field(
        proto.ENUM,
        number=2,
        enum=HarmProbability,
    )
    blocked: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class CitationMetadata(proto.Message):
    r"""A collection of source attributions for a piece of content.

    Attributes:
        citations (MutableSequence[google.cloud.aiplatform_v1beta1.types.Citation]):
            Output only. List of citations.
    """

    citations: MutableSequence["Citation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Citation",
    )


class Citation(proto.Message):
    r"""Source attributions for content.

    Attributes:
        start_index (int):
            Output only. Start index into the content.
        end_index (int):
            Output only. End index into the content.
        uri (str):
            Output only. Url reference of the
            attribution.
        title (str):
            Output only. Title of the attribution.
        license_ (str):
            Output only. License of the attribution.
        publication_date (google.type.date_pb2.Date):
            Output only. Publication date of the
            attribution.
    """

    start_index: int = proto.Field(
        proto.INT32,
        number=1,
    )
    end_index: int = proto.Field(
        proto.INT32,
        number=2,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    title: str = proto.Field(
        proto.STRING,
        number=4,
    )
    license_: str = proto.Field(
        proto.STRING,
        number=5,
    )
    publication_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=6,
        message=date_pb2.Date,
    )


class Candidate(proto.Message):
    r"""A response candidate generated from the model.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        index (int):
            Output only. Index of the candidate.
        content (google.cloud.aiplatform_v1beta1.types.Content):
            Output only. Content parts of the candidate.
        finish_reason (google.cloud.aiplatform_v1beta1.types.Candidate.FinishReason):
            Output only. The reason why the model stopped
            generating tokens. If empty, the model has not
            stopped generating the tokens.
        safety_ratings (MutableSequence[google.cloud.aiplatform_v1beta1.types.SafetyRating]):
            Output only. List of ratings for the safety
            of a response candidate.
            There is at most one rating per category.
        finish_message (str):
            Output only. Describes the reason the mode stopped
            generating tokens in more detail. This is only filled when
            ``finish_reason`` is set.

            This field is a member of `oneof`_ ``_finish_message``.
        citation_metadata (google.cloud.aiplatform_v1beta1.types.CitationMetadata):
            Output only. Source attribution of the
            generated content.
    """

    class FinishReason(proto.Enum):
        r"""The reason why the model stopped generating tokens.
        If empty, the model has not stopped generating the tokens.

        Values:
            FINISH_REASON_UNSPECIFIED (0):
                The finish reason is unspecified.
            STOP (1):
                Natural stop point of the model or provided
                stop sequence.
            MAX_TOKENS (2):
                The maximum number of tokens as specified in
                the request was reached.
            SAFETY (3):
                The token generation was stopped as the
                response was flagged for safety reasons. NOTE:
                When streaming the Candidate.content will be
                empty if content filters blocked the output.
            RECITATION (4):
                The token generation was stopped as the
                response was flagged for unauthorized citations.
            OTHER (5):
                All other reasons that stopped the token
                generation
        """
        FINISH_REASON_UNSPECIFIED = 0
        STOP = 1
        MAX_TOKENS = 2
        SAFETY = 3
        RECITATION = 4
        OTHER = 5

    index: int = proto.Field(
        proto.INT32,
        number=1,
    )
    content: "Content" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Content",
    )
    finish_reason: FinishReason = proto.Field(
        proto.ENUM,
        number=3,
        enum=FinishReason,
    )
    safety_ratings: MutableSequence["SafetyRating"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="SafetyRating",
    )
    finish_message: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    citation_metadata: "CitationMetadata" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="CitationMetadata",
    )


__all__ = tuple(sorted(__protobuf__.manifest))