from typing import Any, Literal


class CPrint:
    def __init__(self, content: Any, print_type: Literal['info', 'error', 'success', 'warning', 'normal'] = "normal"):
        theme = {
            "success": '\033[92m',
            "error": '\033[91m',
            "info": '\033[94m',
            "warning": '\033[93m',
            "normal": '\033[0m',
            "reset": '\033[0m',
        }
        if not isinstance(content, str):
            raise TypeError('The content argument must be a string.')

        self.content = content
        self.reset = theme['reset']
        self.color = theme[print_type]
        if print_type != 'normal' and print_type in ['info', 'error', 'success', 'warning', 'normal']:
            self.colored_print()
        elif print_type == 'normal':
            self.normal_print()
        else:
            raise ValueError("Print argument must be in 'info', 'error', 'success', 'warning', 'normal'.")

    def normal_print(self):
        print(self.content)

    def colored_print(self):
        print(f"{self.color}{self.content}{self.reset}")

    @staticmethod
    def line_break():
        print()

    @staticmethod
    def double_line_break():
        print()
        print()

    @staticmethod
    def divider(content: str = '', spaced_top: bool = False, spaced_bottom: bool = False):
        prev_divider = next_divider = '----------'

        if spaced_top:
            print()

        if content is not None:
            if not isinstance(content, str):
                raise TypeError('Content must be a string.')

            print(prev_divider + ' ' + content + ' ' + next_divider)
        else:
            print(prev_divider + next_divider)

        if spaced_bottom:
            print()
