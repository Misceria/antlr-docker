

import sys
from antlr4 import *
from KilogramParser import KilogramParser
from KilogramLexer import KilogramLexer
from KilogramListener import KilogramListener
from antlr4.error.ErrorListener import ErrorListener


class KilogrammarListener(KilogramListener):


    def __init__(self):
        super().__init__()
        print("Listener activated!")

    def enterProgram(self, ctx: KilogramParser.ProgramContext):
        print("Начато прослушивание общего кода программы")

    def exitProgram(self, ctx: KilogramParser.ProgramContext):
        print("Закончено прослушивание общего кода программы")

    def enterBlock(self, ctx: KilogramParser.BlockContext):
        print("Начат новый блок кода")

    def exitBlock(self, ctx: KilogramParser.BlockContext):
        print("Закрыт блок кода")

    def enterAssignsint(self, ctx: KilogramParser.AssignsintContext):
        print(f"Переменной {ctx.ID()[0].getText()} присвоено целочисленное значение {ctx.INT()[0].getText()}")

    def exitAssignsint(self, ctx: KilogramParser.AssignsintContext):
        pass

    def enterAssignbool(self, ctx: KilogramParser.AssignsintContext):
        print(f"Переменной {ctx.ID()[0].getText()} присвоено булево значение {ctx.BOOL()[0].getText()}")

    def exitAssignbool(self, ctx: KilogramParser.AssignsintContext):
        pass

    def enterAssignsstring(self, ctx: KilogramParser.AssignsintContext):
        print(f"Переменной {ctx.ID()[0].getText()} присвоено булево значение {ctx.STRING()[0].getText()}")

    def exitAssignsstring(self, ctx: KilogramParser.AssignsintContext):
        pass

    def enterAssignmass(self, ctx: KilogramParser.AssignsintContext):
        print(f"Начато создание массива")
        self.array = []

    def exitAssignmass(self, ctx: KilogramParser.AssignsintContext):
        print(f"Получен массив {self.array}\nЗакончено создание массива")

    def enterArray(self, ctx:KilogramParser.ArrayContext):
        self.array.append(ctx.INT().getText())

    def enterSum(self, ctx: KilogramParser.SumContext):
        print(f"Производится операция {ctx.OPER()} между {ctx.sum1().getText()} и {ctx.sum2().getText()}")

    def exitSum(self, ctx: KilogramParser.SumContext):
        pass

    def enterInput(self, ctx:KilogramParser.InputContext):
        print(f"Введена новая переменная {ctx.ID()}")

    def exitInput(self, ctx: KilogramParser.InputContext):
        pass

    def enterBody(self, ctx: KilogramParser.BodyContext):
        pass

    def exitBody(self, ctx: KilogramParser.BodyContext):
        pass

    def enterCycle(self, ctx: KilogramParser.CycleContext):
        print(f"Начат цикл")

    def exitCycle(self, ctx: KilogramParser.CycleContext):
        print(f"Окончен цикл")

    def enterCondition(self, ctx:KilogramParser.ConditionContext):
        print(f"Задано условие выхода из цикла: когда между {ctx.oper1().getText()} и {ctx.oper2().getText()} перестанет выполняться операция {ctx.COMPARE()}")


class KilogrammarErrorListener(ErrorListener):

    def __init__(self):
        print(f"Инициализирован собственный обработчик ошибок KilogrammarErrorListener %")

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nСинтаксическая ошибка возникла в {line} строке {column} колонке.\n Текст сообщения об ошибке: {msg}\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        exit()


def main(arg):
    istream = FileStream(arg)
    lexer = KilogramLexer(istream)
    stream = CommonTokenStream(lexer)
    parser = KilogramParser(stream)

    error_listener = KilogrammarErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()
    printer = KilogrammarListener()
    walker = ParseTreeWalker()

    walker.walk(printer, tree)

    print("Finished.")


if __name__ == '__main__':
    #main(sys.argv)
    #main("train.txt")
    main("ComplexExample.txt")
    #main("ErrorExample.txt")

