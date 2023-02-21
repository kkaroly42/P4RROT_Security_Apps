ingress = bfrt.knocking.pipe.SwitchIngress


def learn_permission_callback(dev_id, pipe_id, direction, parser_id, session, msg):
    global ingress
    for dig in msg:
        ingress.exact_match_table_uid4.add_with_setter_action_uid5_true(dig["src_uid8"])
        print(dig)
    return 0


bfrt.knocking.pipe.SwitchIngressDeparser.generated_digest_uid9.callback_register(
    learn_permission_callback
)

ingress.exact_match_table_uid6.add_with_setter_action_uid7_true(10002)
ingress.set_digest_or_drop_table_uid10.add_with_setter_action_uid11(10002)
ingress.forward.add_with_send("42:19:8e:09:9a:0c",0)
ingress.forward.add_with_send("0a:3d:fd:0f:fc:e8",1)
ingress.forward.add_with_send("ff:ff:ff:ff:ff:ff",1)
ingress.exact_match_table_uid4.add_with_setter_action_uid5_true("11.0.0.5")