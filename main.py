from manim import *
import numpy as np

# manim -pqh main.py EMproblem
class HelloCircle(Scene):
    def construct(self):
        circle = Circle(color=BLUE, fill_opacity=0.5)

        label = Text("A wild circle appears!")
        label.next_to(circle, UP, buff=0.5)

        self.play(Create(circle))
        self.play(Write(label))
        self.wait()


class TransformEquation(Scene):
    def construct(self):
        eq1 = MathTex("42 {{ a^2 }} + {{ b^2 }} = {{ c^2 }}")
        eq2 = MathTex("42 {{ a^2 }} = {{ c^2 }} - {{ b^2 }}")
        eq3 = MathTex(r"a^2 = \frac{c^2 - b^2}{42}")
        eq4 = MathTex(r"\sqrt{a^2} = \sqrt{\frac{c^2 - b^2}{42}}")
        eq5 = MathTex(r"a = \sqrt{\frac{c^2 - b^2}{42}}")
        self.add(eq1)
        self.wait()
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait()
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait()
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait()
        self.play(TransformMatchingTex(eq4, eq5))
        self.wait()


class EMproblem(Scene):
    def construct(self):
        dot = Dot(color=BLUE)
        label_Q = MathTex(r"Q", font_size=30)
        label_Q.next_to(dot, UP + LEFT, buff=0.1)
        dotted_circle = DashedVMobject(Circle(color=BLUE, radius=2))
        line = Line(dot.get_center(), dotted_circle.get_center() + 2 * RIGHT, color=BLUE)
        arrow = {}
        amount_of_arrows = 10
        for i in range(amount_of_arrows+1):
            arrow[i] = Arrow(start=dot.get_center() + 0.5 * (np.sin(2*np.pi*i/9)*LEFT+np.cos(2*np.pi*i/9)*UP), end=dotted_circle.get_center() + 1.5 * (np.sin(2*np.pi*i/9)*LEFT+np.cos(2*np.pi*i/9)*UP), color=BLUE)
        label_E = MathTex(r"\vec{E}", font_size=30)
        label_E.next_to(arrow[0], RIGHT, buff=0.1)
        label_r = MathTex(r"r", font_size=30)
        label_r.next_to(line, DOWN, buff=0.1)

        self.play(Create(dot), Write(label_Q))
        self.wait()
        animations = [Create(arrow[i]) for i in range(amount_of_arrows+1)]
        self.play(*animations, Write(label_E))
        self.wait()
        self.play(Create(dotted_circle), Create(line), Write(label_r))
        self.wait()
        self.play(Transform(dotted_circle, DashedVMobject(Circle(color=BLUE, radius=3))), Transform(line, Line(dot.get_center(), dotted_circle.get_center() + 3 * RIGHT, color=BLUE)), label_r.animate.next_to(Line(dot.get_center(), dotted_circle.get_center() + 3 * RIGHT, color=BLUE), DOWN, buff=0.1))
        self.wait(0.5)
        self.play(Transform(dotted_circle, DashedVMobject(Circle(color=BLUE, radius=1))), Transform(line, Line(dot.get_center(), dotted_circle.get_center() + 1 * RIGHT, color=BLUE)), label_r.animate.next_to(Line(dot.get_center(), dotted_circle.get_center() + 1 * RIGHT, color=BLUE), DOWN, buff=0.1))
        self.wait(0.5)
        self.play(Transform(dotted_circle, DashedVMobject(Circle(color=BLUE, radius=2))), Transform(line, Line(dot.get_center(), dotted_circle.get_center() + 2 * RIGHT, color=BLUE)), label_r.animate.next_to(Line(dot.get_center(), dotted_circle.get_center() + 2 * RIGHT, color=BLUE), DOWN, buff=0.1))
        self.wait()
        movement = 5 * LEFT + 1.5 * UP
        group = Group(dot, label_Q, dotted_circle, line, label_r, label_E,
                      *[arrow[i] for i in range(amount_of_arrows+1)])
        self.play(group.animate.shift(movement))
        self.wait(3)
        pos1 = 2 * RIGHT + 1.5 * UP
        pos2 = 3 * RIGHT
        announcement = Text("Let's use Gauss' law to\n find the electric field!", font_size=25).shift(pos1)
        eq1 = MathTex(r"\oint \vec{E} \cdot d\vec{A} = \frac{Q}{\varepsilon_0}").shift(pos2)
        r1 = Text(r"Since \vec{E} and d\vec{A} are parallel, we have", font_size=25).shift(pos1)
        eq2 = MathTex(r"\oint EdA = \frac{Q}{\varepsilon_0}").shift(pos2)
        r2 = Text(r"Since \vec{E} is constant over the Gaussian surface, we have", font_size=25).shift(pos1)
        eq3 = MathTex(r"E \oint dA = \frac{Q}{\varepsilon_0}").shift(pos2)
        r3 = Text(r"Since the Gaussian surface is a circle, we have", font_size=25).shift(pos1)
        eq4 = MathTex(r"E \cdot4\pi r^2 = \frac{Q}{\varepsilon_0}").shift(pos2)
        eq5 = MathTex(r"E = \frac{Q}{4\pi\varepsilon_0 r^2}").shift(pos2)
        eq6 = MathTex(r"\vec{E} = \frac{Q}{4\pi\varepsilon_0} \frac{1}{r^2}\hat{r}").shift(pos2)

        self.play(Write(announcement))
        self.wait(2)
        self.play(Write(eq1))
        self.wait(2)
        self.play(Transform(announcement, r1))
        self.wait(2)
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(2)
        self.play(Transform(announcement, r2))
        self.wait(2)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(2)
        self.play(Transform(announcement, r3))
        self.wait(2)
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait(2)
        self.play(TransformMatchingTex(eq4, eq5))
        self.wait(2)
        self.play(TransformMatchingTex(eq5, eq6))

        self.play(Uncreate(dotted_circle), Uncreate(line), Uncreate(dot), Uncreate(label_Q), Uncreate(label_r))


