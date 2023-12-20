# Generated from C:/Users/klopp/PycharmProjects/ANTLR/Kilogram.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .KilogramParser import KilogramParser
else:
    from KilogramParser import KilogramParser

# This class defines a complete generic visitor for a parse tree produced by KilogramParser.

class KilogramVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by KilogramParser#startRule.
    def visitStartRule(self, ctx:KilogramParser.StartRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KilogramParser#program.
    def visitProgram(self, ctx:KilogramParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KilogramParser#assignbool.
    def visitAssignbool(self, ctx:KilogramParser.AssignboolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KilogramParser#assignsstring.
    def visitAssignsstring(self, ctx:KilogramParser.AssignsstringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KilogramParser#var.
    def visitVar(self, ctx:KilogramParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KilogramParser#numvar.
    def visitNumvar(self, ctx:KilogramParser.NumvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KilogramParser#assignsint.
    def visitAssignsint(self, ctx:KilogramParser.AssignsintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KilogramParser#array.
    def visitArray(self, ctx:KilogramParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KilogramParser#assignmass.
    def visitAssignmass(self, ctx:KilogramParser.AssignmassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KilogramParser#sum1.
    def visitSum1(self, ctx:KilogramParser.Sum1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KilogramParser#sum2.
    def visitSum2(self, ctx:KilogramParser.Sum2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KilogramParser#sum.
    def visitSum(self, ctx:KilogramParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KilogramParser#input.
    def visitInput(self, ctx:KilogramParser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KilogramParser#body.
    def visitBody(self, ctx:KilogramParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KilogramParser#block.
    def visitBlock(self, ctx:KilogramParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KilogramParser#cycle.
    def visitCycle(self, ctx:KilogramParser.CycleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KilogramParser#oper1.
    def visitOper1(self, ctx:KilogramParser.Oper1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KilogramParser#oper2.
    def visitOper2(self, ctx:KilogramParser.Oper2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KilogramParser#condition.
    def visitCondition(self, ctx:KilogramParser.ConditionContext):
        return self.visitChildren(ctx)



del KilogramParser