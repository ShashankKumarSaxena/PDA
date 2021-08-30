.. currentmodule:: discord

API Reference
===============

The following section outlines the API of pda.py's command extension module.

.. _ext_commands_api_bot:

Bots
------

Bot
~~~~

.. attributetable:: pda.ext.commands.Bot

.. autoclass:: pda.ext.commands.Bot
    :members:
    :inherited-members:
    :exclude-members: after_invoke, before_invoke, check, check_once, command, event, group, listen

    .. automethod:: Bot.after_invoke()
        :decorator:

    .. automethod:: Bot.before_invoke()
        :decorator:

    .. automethod:: Bot.check()
        :decorator:

    .. automethod:: Bot.check_once()
        :decorator:

    .. automethod:: Bot.command(*args, **kwargs)
        :decorator:
    
    .. automethod:: Bot.event()
        :decorator:

    .. automethod:: Bot.group(*args, **kwargs)
        :decorator:

    .. automethod:: Bot.listen(name=None)
        :decorator:

AutoShardedBot
~~~~~~~~~~~~~~~~

.. attributetable:: pda.ext.commands.AutoShardedBot

.. autoclass:: pda.ext.commands.AutoShardedBot
    :members:

Prefix Helpers
----------------

.. autofunction:: pda.ext.commands.when_mentioned

.. autofunction:: pda.ext.commands.when_mentioned_or

.. _ext_commands_api_events:

Event Reference
-----------------

These events function similar to :ref:`the regular events <discord-api-events>`, except they
are custom to the command extension module.

.. function:: pda.ext.commands.on_command_error(ctx, error)

    An error handler that is called when an error is raised
    inside a command either through user input error, check
    failure, or an error in your own code.

    A default one is provided (:meth:`.Bot.on_command_error`).

    :param ctx: The invocation context.
    :type ctx: :class:`.Context`
    :param error: The error that was raised.
    :type error: :class:`.CommandError` derived

.. function:: pda.ext.commands.on_command(ctx)

    An event that is called when a command is found and is about to be invoked.

    This event is called regardless of whether the command itself succeeds via
    error or completes.

    :param ctx: The invocation context.
    :type ctx: :class:`.Context`

.. function:: pda.ext.commands.on_command_completion(ctx)

    An event that is called when a command has completed its invocation.

    This event is called only if the command succeeded, i.e. all checks have
    passed and the user input it correctly.

    :param ctx: The invocation context.
    :type ctx: :class:`.Context`

.. _ext_commands_api_command:

Commands
----------

Decorators
~~~~~~~~~~~~

.. autofunction:: pda.ext.commands.command
    :decorator:

.. autofunction:: pda.ext.commands.group
    :decorator:

Command
~~~~~~~~~

.. attributetable:: pda.ext.commands.Command

.. autoclass:: pda.ext.commands.Command
    :members:
    :special-members: __call__
    :exclude-members: after_invoke, before_invoke, error

    .. automethod:: Command.after_invoke()
        :decorator:

    .. automethod:: Command.before_invoke()
        :decorator:

    .. automethod:: Command.error()
        :decorator:

Group
~~~~~~

.. attributetable:: pda.ext.commands.Group

.. autoclass:: pda.ext.commands.Group
    :members:
    :inherited-members:
    :exclude-members: after_invoke, before_invoke, command, error, group

    .. automethod:: Group.after_invoke()
        :decorator:

    .. automethod:: Group.before_invoke()
        :decorator:

    .. automethod:: Group.command(*args, **kwargs)
        :decorator:

    .. automethod:: Group.error()
        :decorator:

    .. automethod:: Group.group(*args, **kwargs)
        :decorator:

GroupMixin
~~~~~~~~~~~

.. attributetable:: pda.ext.commands.GroupMixin

.. autoclass:: pda.ext.commands.GroupMixin
    :members:
    :exclude-members: command, group

    .. automethod:: GroupMixin.command(*args, **kwargs)
        :decorator:

    .. automethod:: GroupMixin.group(*args, **kwargs)
        :decorator:

.. _ext_commands_api_cogs:

Cogs
------

Cog
~~~~

.. attributetable:: pda.ext.commands.Cog

.. autoclass:: pda.ext.commands.Cog
    :members:

CogMeta
~~~~~~~~

.. attributetable:: pda.ext.commands.CogMeta

.. autoclass:: pda.ext.commands.CogMeta
    :members:

.. _ext_commands_help_command:

Help Commands
---------------

HelpCommand
~~~~~~~~~~~~

.. attributetable:: pda.ext.commands.HelpCommand

.. autoclass:: pda.ext.commands.HelpCommand
    :members:

DefaultHelpCommand
~~~~~~~~~~~~~~~~~~~

.. attributetable:: pda.ext.commands.DefaultHelpCommand

.. autoclass:: pda.ext.commands.DefaultHelpCommand
    :members:
    :exclude-members: send_bot_help, send_cog_help, send_group_help, send_command_help, prepare_help_command

MinimalHelpCommand
~~~~~~~~~~~~~~~~~~~

.. attributetable:: pda.ext.commands.MinimalHelpCommand

.. autoclass:: pda.ext.commands.MinimalHelpCommand
    :members:
    :exclude-members: send_bot_help, send_cog_help, send_group_help, send_command_help, prepare_help_command

Paginator
~~~~~~~~~~

.. attributetable:: pda.ext.commands.Paginator

.. autoclass:: pda.ext.commands.Paginator
    :members:

Enums
------

.. class:: BucketType
    :module: pda.ext.commands

    Specifies a type of bucket for, e.g. a cooldown.

    .. attribute:: default

        The default bucket operates on a global basis.
    .. attribute:: user

        The user bucket operates on a per-user basis.
    .. attribute:: guild

        The guild bucket operates on a per-guild basis.
    .. attribute:: channel

        The channel bucket operates on a per-channel basis.
    .. attribute:: member

        The member bucket operates on a per-member basis.
    .. attribute:: category

        The category bucket operates on a per-category basis.
    .. attribute:: role

        The role bucket operates on a per-role basis.

        .. versionadded:: 1.3


.. _ext_commands_api_checks:

Checks
-------

.. autofunction:: pda.ext.commands.check(predicate)
    :decorator:

.. autofunction:: pda.ext.commands.check_any(*checks)
    :decorator:

.. autofunction:: pda.ext.commands.has_role(item)
    :decorator:

.. autofunction:: pda.ext.commands.has_permissions(**perms)
    :decorator:

.. autofunction:: pda.ext.commands.has_guild_permissions(**perms)
    :decorator:

.. autofunction:: pda.ext.commands.has_any_role(*items)
    :decorator:

.. autofunction:: pda.ext.commands.bot_has_role(item)
    :decorator:

.. autofunction:: pda.ext.commands.bot_has_permissions(**perms)
    :decorator:

.. autofunction:: pda.ext.commands.bot_has_guild_permissions(**perms)
    :decorator:

.. autofunction:: pda.ext.commands.bot_has_any_role(*items)
    :decorator:

.. autofunction:: pda.ext.commands.cooldown(rate, per, type=pda.ext.commands.BucketType.default)
    :decorator:

.. autofunction:: pda.ext.commands.dynamic_cooldown(cooldown, type=BucketType.default)
    :decorator:

.. autofunction:: pda.ext.commands.max_concurrency(number, per=pda.ext.commands.BucketType.default, *, wait=False)
    :decorator:

.. autofunction:: pda.ext.commands.before_invoke(coro)
    :decorator:

.. autofunction:: pda.ext.commands.after_invoke(coro)
    :decorator:

.. autofunction:: pda.ext.commands.guild_only(,)
    :decorator:

.. autofunction:: pda.ext.commands.dm_only(,)
    :decorator:

.. autofunction:: pda.ext.commands.is_owner(,)
    :decorator:

.. autofunction:: pda.ext.commands.is_nsfw(,)
    :decorator:

.. _ext_commands_api_context:

Cooldown
---------

.. attributetable:: pda.ext.commands.Cooldown

.. autoclass:: pda.ext.commands.Cooldown
    :members:

Context
--------

.. attributetable:: pda.ext.commands.Context

.. autoclass:: pda.ext.commands.Context
    :members:
    :inherited-members:
    :exclude-members: history, typing

    .. automethod:: pda.ext.commands.Context.history
        :async-for:

    .. automethod:: pda.ext.commands.Context.typing
        :async-with:

.. _ext_commands_api_converters:

Converters
------------

.. autoclass:: pda.ext.commands.Converter
    :members:

.. autoclass:: pda.ext.commands.ObjectConverter
    :members:

.. autoclass:: pda.ext.commands.MemberConverter
    :members:

.. autoclass:: pda.ext.commands.UserConverter
    :members:

.. autoclass:: pda.ext.commands.MessageConverter
    :members:

.. autoclass:: pda.ext.commands.PartialMessageConverter
    :members:

.. autoclass:: pda.ext.commands.GuildChannelConverter
    :members:

.. autoclass:: pda.ext.commands.TextChannelConverter
    :members:

.. autoclass:: pda.ext.commands.VoiceChannelConverter
    :members:

.. autoclass:: pda.ext.commands.StoreChannelConverter
    :members:

.. autoclass:: pda.ext.commands.StageChannelConverter
    :members:

.. autoclass:: pda.ext.commands.CategoryChannelConverter
    :members:

.. autoclass:: pda.ext.commands.InviteConverter
    :members:

.. autoclass:: pda.ext.commands.GuildConverter
    :members:

.. autoclass:: pda.ext.commands.RoleConverter
    :members:

.. autoclass:: pda.ext.commands.GameConverter
    :members:

.. autoclass:: pda.ext.commands.ColourConverter
    :members:

.. autoclass:: pda.ext.commands.EmojiConverter
    :members:

.. autoclass:: pda.ext.commands.PartialEmojiConverter
    :members:

.. autoclass:: pda.ext.commands.ThreadConverter
    :members:

.. autoclass:: pda.ext.commands.GuildStickerConverter
    :members:

.. autoclass:: pda.ext.commands.clean_content
    :members:

.. autoclass:: pda.ext.commands.Greedy()

.. autofunction:: pda.ext.commands.run_converters

Flag Converter
~~~~~~~~~~~~~~~

.. autoclass:: pda.ext.commands.FlagConverter
    :members:

.. autoclass:: pda.ext.commands.Flag()
    :members:

.. autofunction:: pda.ext.commands.flag

.. _ext_commands_api_errors:

Exceptions
-----------

.. autoexception:: pda.ext.commands.CommandError
    :members:

.. autoexception:: pda.ext.commands.ConversionError
    :members:

.. autoexception:: pda.ext.commands.MissingRequiredArgument
    :members:

.. autoexception:: pda.ext.commands.ArgumentParsingError
    :members:

.. autoexception:: pda.ext.commands.UnexpectedQuoteError
    :members:

.. autoexception:: pda.ext.commands.InvalidEndOfQuotedStringError
    :members:

.. autoexception:: pda.ext.commands.ExpectedClosingQuoteError
    :members:

.. autoexception:: pda.ext.commands.BadArgument
    :members:

.. autoexception:: pda.ext.commands.BadUnionArgument
    :members:

.. autoexception:: pda.ext.commands.BadLiteralArgument
    :members:

.. autoexception:: pda.ext.commands.PrivateMessageOnly
    :members:

.. autoexception:: pda.ext.commands.NoPrivateMessage
    :members:

.. autoexception:: pda.ext.commands.CheckFailure
    :members:

.. autoexception:: pda.ext.commands.CheckAnyFailure
    :members:

.. autoexception:: pda.ext.commands.CommandNotFound
    :members:

.. autoexception:: pda.ext.commands.DisabledCommand
    :members:

.. autoexception:: pda.ext.commands.CommandInvokeError
    :members:

.. autoexception:: pda.ext.commands.TooManyArguments
    :members:

.. autoexception:: pda.ext.commands.UserInputError
    :members:

.. autoexception:: pda.ext.commands.CommandOnCooldown
    :members:

.. autoexception:: pda.ext.commands.MaxConcurrencyReached
    :members:

.. autoexception:: pda.ext.commands.NotOwner
    :members:

.. autoexception:: pda.ext.commands.MessageNotFound
    :members:

.. autoexception:: pda.ext.commands.MemberNotFound
    :members:

.. autoexception:: pda.ext.commands.GuildNotFound
    :members:

.. autoexception:: pda.ext.commands.UserNotFound
    :members:

.. autoexception:: pda.ext.commands.ChannelNotFound
    :members:

.. autoexception:: pda.ext.commands.ChannelNotReadable
    :members:

.. autoexception:: pda.ext.commands.ThreadNotFound
    :members:

.. autoexception:: pda.ext.commands.BadColourArgument
    :members:

.. autoexception:: pda.ext.commands.RoleNotFound
    :members:

.. autoexception:: pda.ext.commands.BadInviteArgument
    :members:

.. autoexception:: pda.ext.commands.EmojiNotFound
    :members:

.. autoexception:: pda.ext.commands.PartialEmojiConversionFailure
    :members:

.. autoexception:: pda.ext.commands.GuildStickerNotFound
    :members:

.. autoexception:: pda.ext.commands.BadBoolArgument
    :members:

.. autoexception:: pda.ext.commands.MissingPermissions
    :members:

.. autoexception:: pda.ext.commands.BotMissingPermissions
    :members:

.. autoexception:: pda.ext.commands.MissingRole
    :members:

.. autoexception:: pda.ext.commands.BotMissingRole
    :members:

.. autoexception:: pda.ext.commands.MissingAnyRole
    :members:

.. autoexception:: pda.ext.commands.BotMissingAnyRole
    :members:

.. autoexception:: pda.ext.commands.NSFWChannelRequired
    :members:

.. autoexception:: pda.ext.commands.FlagError
    :members:

.. autoexception:: pda.ext.commands.BadFlagArgument
    :members:

.. autoexception:: pda.ext.commands.MissingFlagArgument
    :members:

.. autoexception:: pda.ext.commands.TooManyFlags
    :members:

.. autoexception:: pda.ext.commands.MissingRequiredFlag
    :members:

.. autoexception:: pda.ext.commands.ExtensionError
    :members:

.. autoexception:: pda.ext.commands.ExtensionAlreadyLoaded
    :members:

.. autoexception:: pda.ext.commands.ExtensionNotLoaded
    :members:

.. autoexception:: pda.ext.commands.NoEntryPointError
    :members:

.. autoexception:: pda.ext.commands.ExtensionFailed
    :members:

.. autoexception:: pda.ext.commands.ExtensionNotFound
    :members:

.. autoexception:: pda.ext.commands.CommandRegistrationError
    :members:


Exception Hierarchy
~~~~~~~~~~~~~~~~~~~~~

.. exception_hierarchy::

    - :exc:`~.DiscordException`
        - :exc:`~.commands.CommandError`
            - :exc:`~.commands.ConversionError`
            - :exc:`~.commands.UserInputError`
                - :exc:`~.commands.MissingRequiredArgument`
                - :exc:`~.commands.TooManyArguments`
                - :exc:`~.commands.BadArgument`
                    - :exc:`~.commands.MessageNotFound`
                    - :exc:`~.commands.MemberNotFound`
                    - :exc:`~.commands.GuildNotFound`
                    - :exc:`~.commands.UserNotFound`
                    - :exc:`~.commands.ChannelNotFound`
                    - :exc:`~.commands.ChannelNotReadable`
                    - :exc:`~.commands.BadColourArgument`
                    - :exc:`~.commands.RoleNotFound`
                    - :exc:`~.commands.BadInviteArgument`
                    - :exc:`~.commands.EmojiNotFound`
                    - :exc:`~.commands.GuildStickerNotFound`
                    - :exc:`~.commands.PartialEmojiConversionFailure`
                    - :exc:`~.commands.BadBoolArgument`
                    - :exc:`~.commands.ThreadNotFound`
                    - :exc:`~.commands.FlagError`
                        - :exc:`~.commands.BadFlagArgument`
                        - :exc:`~.commands.MissingFlagArgument`
                        - :exc:`~.commands.TooManyFlags`
                        - :exc:`~.commands.MissingRequiredFlag`
                - :exc:`~.commands.BadUnionArgument`
                - :exc:`~.commands.BadLiteralArgument`
                - :exc:`~.commands.ArgumentParsingError`
                    - :exc:`~.commands.UnexpectedQuoteError`
                    - :exc:`~.commands.InvalidEndOfQuotedStringError`
                    - :exc:`~.commands.ExpectedClosingQuoteError`
            - :exc:`~.commands.CommandNotFound`
            - :exc:`~.commands.CheckFailure`
                - :exc:`~.commands.CheckAnyFailure`
                - :exc:`~.commands.PrivateMessageOnly`
                - :exc:`~.commands.NoPrivateMessage`
                - :exc:`~.commands.NotOwner`
                - :exc:`~.commands.MissingPermissions`
                - :exc:`~.commands.BotMissingPermissions`
                - :exc:`~.commands.MissingRole`
                - :exc:`~.commands.BotMissingRole`
                - :exc:`~.commands.MissingAnyRole`
                - :exc:`~.commands.BotMissingAnyRole`
                - :exc:`~.commands.NSFWChannelRequired`
            - :exc:`~.commands.DisabledCommand`
            - :exc:`~.commands.CommandInvokeError`
            - :exc:`~.commands.CommandOnCooldown`
            - :exc:`~.commands.MaxConcurrencyReached`
        - :exc:`~.commands.ExtensionError`
            - :exc:`~.commands.ExtensionAlreadyLoaded`
            - :exc:`~.commands.ExtensionNotLoaded`
            - :exc:`~.commands.NoEntryPointError`
            - :exc:`~.commands.ExtensionFailed`
            - :exc:`~.commands.ExtensionNotFound`
    - :exc:`~.ClientException`
        - :exc:`~.commands.CommandRegistrationError`
