from First_text.re_test_patterns_groups import text_patterns

text_patterns('abbaabbba',[(r'a((a*)(b*))','a followed by 0-n a and 0-n b')],)


