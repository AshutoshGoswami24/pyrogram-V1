#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2021 Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.


from typing import Callable

import pyrogram
from pyrogram.scaffold import Scaffold


class OnError(Scaffold):
    def on_error(
        self=None,
        catch_all: bool = False,
    ) -> callable:
        """Decorator for handling errors.

        This does the same thing as :meth:`~pyrogram.Client.add_handler` using the
        :obj:`~pyrogram.handlers.ErrorHandler`.

        Parameters:
            catch_all (`bool`, *optional*):
                Pass true in order to catch every error (not only RPCError) on your app.

        """

        def decorator(function: Callable) -> Callable:
            self.add_handler(
                pyrogram.handlers.error_handler.ErrorHandler(self, function, catch_all)
            )
            return function

        return decorator
