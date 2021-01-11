img = Graphics[
	{
		RGBColor[0.1,0.3,0.3], Rectangle[{0,0}, {1,1}],
		Text[Style["cq", FontSize->19, FontFamily->"Roboto", Bold, White],{0.5, 0.5}],
		GrayLevel[0.9], Rectangle[{1,0}, {9,1}],
		Text[Style["Functional Testing Project", FontSize->18, FontFamily->"Roboto Mono", Black],{5, 0.5}]
	}
]

Export["cq_testing.svg", img]
