.. currentmodule:: discord

API Reference
===============

The following section outlines the API of PDA.py's command extension module.

.. _ext_commands_api_bot:

Bots
------

Bot
~~~~

.. attributetable:: PDA.ext.commands.Bot

.. autoclass:: PDA.ext.commands.Bot
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

.. attributetable:: PDA.ext.commands.AutoShardedBot

.. autoclass:: PDA.ext.commands.AutoShardedBot
    :members:

Prefix Helpers
----------------

.. autofunction:: PDA.ext.commands.when_mentioned

.. autofunction:: PDA.ext.commands.when_mentioned_or

.. _ext_commands_api_events:

Event Reference
-----------------

These events function similar to :ref:`the regular events <discord-api-events>`, except they
are custom to the command extension module.

.. function:: PDA.ext.commands.on_command_error(ctx, error)

    An error handler that is called when an error is raised
    inside a command either through user input error, check
    failure, or an error in your own code.

    A default one is provided (:meth:`.Bot.on_command_error`).

    :param ctx: The invocation context.
    :type ctx: :class:`.Context`
    :param error: The error that was raised.
    :type error: :class:`.CommandError` derived

.. function:: PDA.ext.commands.on_command(ctx)

    An event that is called when a command is found and is about to be invoked.

    This event is called regardless of whether the command itself succeeds via
    error or completes.

    :param ctx: The invocation context.
    :type ctx: :class:`.Context`

.. function:: PDA.ext.commands.on_command_completion(ctx)

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

.. autofunction:: PDA.ext.commands.command
    :decorator:

.. autofunction:: PDA.ext.commands.group
    :decorator:

Command
~~~~~~~~~

.. attributetable:: PDA.ext.commands.Command

.. autoclass:: PDA.ext.commands.Command
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

.. attributetable:: PDA.ext.commands.Group

.. autoclass:: PDA.ext.commands.Group
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

.. attributetable:: PDA.ext.commands.GroupMixin

.. autoclass:: PDA.ext.commands.GroupMixin
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

.. attributetable:: PDA.ext.commands.Cog

.. autoclass:: PDA.ext.commands.Cog
    :members:

CogMeta
~~~~~~~~

.. attributetable:: PDA.ext.commands.CogMeta

.. autoclass:: PDA.ext.commands.CogMeta
    :members:

.. _ext_commands_help_command:

Help Commands
---------------

HelpCommand
~~~~~~~~~~~~

.. attributetable:: PDA.ext.commands.HelpCommand

.. autoclass:: PDA.ext.commands.HelpCommand
    :members:

DefaultHelpCommand
~~~~~~~~~~~~~~~~~~~

.. attributetable:: PDA.ext.commands.DefaultHelpCommand

.. autoclass:: PDA.ext.commands.DefaultHelpCommand
    :members:
    :exclude-members: send_bot_help, send_cog_help, send_group_help, send_command_help, prepare_help_command

MinimalHelpCommand
~~~~~~~~~~~~~~~~~~~

.. attributetable:: PDA.ext.commands.MinimalHelpCommand

.. autoclass:: PDA.ext.commands.MinimalHelpCommand
    :members:
    :exclude-members: send_bot_help, send_cog_help, send_group_help, send_command_help, prepare_help_command

Paginator
~~~~~~~~~~

.. attributetable:: PDA.ext.commands.Paginator

.. autoclass:: PDA.ext.commands.Paginator
    :members:

Enums
------

.. class:: BucketType
    :module: PDA.ext.commands

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

.. autofunction:: PDA.ext.commands.check(predicate)
    :decorator:

.. autofunction:: PDA.ext.commands.check_any(*checks)
    :decorator:

.. autofunction:: PDA.ext.commands.has_role(item)
    :decorator:

.. autofunction:: PDA.ext.commands.has_permissions(**perms)
    :decorator:

.. autofunction:: PDA.ext.commands.has_guild_permissions(**perms)
    :decorator:

.. autofunction:: PDA.ext.commands.has_any_role(*items)
    :decorator:

.. autofunction:: PDA.ext.commands.bot_has_role(item)
    :decorator:

.. autofunction:: PDA.ext.commands.bot_has_permissions(**perms)
    :decorator:

.. autofunction:: PDA.ext.commands.bot_has_guild_permissions(**perms)
    :decorator:

.. autofunction:: PDA.ext.commands.bot_has_any_role(*items)
    :decorator:

.. autofunction:: PDA.ext.commands.cooldown(rate, per, type=PDA.ext.commands.BucketType.default)
    :decorator:

.. autofunction:: PDA.ext.commands.dynamic_cooldown(cooldown, type=BucketType.default)
    :decorator:

.. autofunction:: PDA.ext.commands.max_concurrency(number, per=PDA.ext.commands.BucketType.default, *, wait=False)
    :decorator:

.. autofunction:: PDA.ext.commands.before_invoke(coro)
    :decorator:

.. autofunction:: PDA.ext.commands.after_invoke(coro)
    :decorator:

.. autofunction:: PDA.ext.commands.guild_only(,)
    :decorator:

.. autofunction:: PDA.ext.commands.dm_only(,)
    :decorator:

.. autofunction:: PDA.ext.commands.is_owner(,)
    :decorator:

.. autofunction:: PDA.ext.commands.is_nsfw(,)
    :decorator:

.. _ext_commands_api_context:

Cooldown
---------

.. attributetable:: PDA.ext.commands.Cooldown

.. autoclass:: PDA.ext.commands.Cooldown
    :members:

Context
--------

.. attributetable:: PDA.ext.commands.Context

.. autoclass:: PDA.ext.commands.Context
    :members:
    :inherited-members:
    :exclude-members: history, typing

    .. automethod:: PDA.ext.commands.Context.history
        :async-for:

    .. automethod:: PDA.ext.commands.Context.typing
        :async-with:

.. _ext_commands_api_converters:

Converters
------------

.. autoclass:: PDA.ext.commands.Converter
    :members:

.. autoclass:: PDA.ext.commands.ObjectConverter
    :members:

.. autoclass:: PDA.ext.commands.MemberConverter
    :members:

.. autoclass:: PDA.ext.commands.UserConverter
    :members:

.. autoclass:: PDA.ext.commands.MessageConverter
    :members:

.. autoclass:: PDA.ext.commands.PartialMessageConverter
    :members:

.. autoclass:: PDA.ext.commands.GuildChannelConverter
    :members:

.. autoclass:: PDA.ext.commands.TextChannelConverter
    :members:

.. autoclass:: PDA.ext.commands.VoiceChannelConverter
    :members:

.. autoclass:: PDA.ext.commands.StoreChannelConverter
    :members:

.. autoclass:: PDA.ext.commands.StageChannelConverter
    :members:

.. autoclass:: PDA.ext.commands.CategoryChannelConverter
    :members:

.. autoclass:: PDA.ext.commands.InviteConverter
    :members:

.. autoclass:: PDA.ext.commands.GuildConverter
    :members:

.. autoclass:: PDA.ext.commands.RoleConverter
    :members:

.. autoclass:: PDA.ext.commands.GameConverter
    :members:

.. autoclass:: PDA.ext.commands.ColourConverter
    :members:

.. autoclass:: PDA.ext.commands.EmojiConverter
    :members:

.. autoclass:: PDA.ext.commands.PartialEmojiConverter
    :members:

.. autoclass:: PDA.ext.commands.ThreadConverter
    :members:

.. autoclass:: PDA.ext.commands.GuildStickerConverter
    :members:

.. autoclass:: PDA.ext.commands.clean_content
    :members:

.. autoclass:: PDA.ext.commands.Greedy()

.. autofunction:: PDA.ext.commands.run_converters

Flag Converter
~~~~~~~~~~~~~~~

.. autoclass:: PDA.ext.commands.FlagConverter
    :members:

.. autoclass:: PDA.ext.commands.Flag()
    :members:

.. autofunction:: PDA.ext.commands.flag

.. _ext_commands_api_errors:

Exceptions
-----------

.. autoexception:: PDA.ext.commands.CommandError
    :members:

.. autoexception:: PDA.ext.commands.ConversionError
    :members:

.. autoexception:: PDA.ext.commands.MissingRequiredArgument
    :members:

.. autoexception:: PDA.ext.commands.ArgumentParsingError
    :members:

.. autoexception:: PDA.ext.commands.UnexpectedQuoteError
    :members:

.. autoexception:: PDA.ext.commands.InvalidEndOfQuotedStringError
    :members:

.. autoexception:: PDA.ext.commands.ExpectedClosingQuoteError
    :members:

.. autoexception:: PDA.ext.commands.BadArgument
    :members:

.. autoexception:: PDA.ext.commands.BadUnionArgument
    :members:

.. autoexception:: PDA.ext.commands.BadLiteralArgument
    :members:

.. autoexception:: PDA.ext.commands.PrivateMessageOnly
    :members:

.. autoexception:: PDA.ext.commands.NoPrivateMessage
    :members:

.. autoexception:: PDA.ext.commands.CheckFailure
    :members:

.. autoexception:: PDA.ext.commands.CheckAnyFailure
    :members:

.. autoexception:: PDA.ext.commands.CommandNotFound
    :members:

.. autoexception:: PDA.ext.commands.DisabledCommand
    :members:

.. autoexception:: PDA.ext.commands.CommandInvokeError
    :members:

.. autoexception:: PDA.ext.commands.TooManyArguments
    :members:

.. autoexception:: PDA.ext.commands.UserInputError
    :members:

.. autoexception:: PDA.ext.commands.CommandOnCooldown
    :members:

.. autoexception:: PDA.ext.commands.MaxConcurrencyReached
    :members:

.. autoexception:: PDA.ext.commands.NotOwner
    :members:

.. autoexception:: PDA.ext.commands.MessageNotFound
    :members:

.. autoexception:: PDA.ext.commands.MemberNotFound
    :members:

.. autoexception:: PDA.ext.commands.GuildNotFound
    :members:

.. autoexception:: PDA.ext.commands.UserNotFound
    :members:

.. autoexception:: PDA.ext.commands.ChannelNotFound
    :members:

.. autoexception:: PDA.ext.commands.ChannelNotReadable
    :members:

.. autoexception:: PDA.ext.commands.ThreadNotFound
    :members:

.. autoexception:: PDA.ext.commands.BadColourArgument
    :members:

.. autoexception:: PDA.ext.commands.RoleNotFound
    :members:

.. autoexception:: PDA.ext.commands.BadInviteArgument
    :members:

.. autoexception:: PDA.ext.commands.EmojiNotFound
    :members:

.. autoexception:: PDA.ext.commands.PartialEmojiConversionFailure
    :members:

.. autoexception:: PDA.ext.commands.GuildStickerNotFound
    :members:

.. autoexception:: PDA.ext.commands.BadBoolArgument
    :members:

.. autoexception:: PDA.ext.commands.MissingPermissions
    :members:

.. autoexception:: PDA.ext.commands.BotMissingPermissions
    :members:

.. autoexception:: PDA.ext.commands.MissingRole
    :members:

.. autoexception:: PDA.ext.commands.BotMissingRole
    :members:

.. autoexception:: PDA.ext.commands.MissingAnyRole
    :members:

.. autoexception:: PDA.ext.commands.BotMissingAnyRole
    :members:

.. autoexception:: PDA.ext.commands.NSFWChannelRequired
    :members:

.. autoexception:: PDA.ext.commands.FlagError
    :members:

.. autoexception:: PDA.ext.commands.BadFlagArgument
    :members:

.. autoexception:: PDA.ext.commands.MissingFlagArgument
    :members:

.. autoexception:: PDA.ext.commands.TooManyFlags
    :members:

.. autoexception:: PDA.ext.commands.MissingRequiredFlag
    :members:

.. autoexception:: PDA.ext.commands.ExtensionError
    :members:

.. autoexception:: PDA.ext.commands.ExtensionAlreadyLoaded
    :members:

.. autoexception:: PDA.ext.commands.ExtensionNotLoaded
    :members:

.. autoexception:: PDA.ext.commands.NoEntryPointError
    :members:

.. autoexception:: PDA.ext.commands.ExtensionFailed
    :members:

.. autoexception:: PDA.ext.commands.ExtensionNotFound
    :members:

.. autoexception:: PDA.ext.commands.CommandRegistrationError
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
