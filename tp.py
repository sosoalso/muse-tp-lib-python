# ---------------------------------------------------------------------------- #
def tp_add_watcher(tp, port, btn, callback):
    """
    tp_add_watcher 함수는 tp 객체의 모든 요소에 대해 지정된 port와 btn에 대한 callback 함수를 등록합니다.
    """
    for t in tp:
        t.port[port].button[btn].watch(callback)
# ---------------------------------------------------------------------------- #
def tp_send_command(tp, port, command):
    """
    tp_send_command 함수는 tp 객체의 모든 요소에 대해 지정된 port와 command를 전송합니다.
    """
    for t in tp:
        if t:
            t.port[port].send_command(command)
# ---------------------------------------------------------------------------- #
def tp_set_button(tp, port, btn, state):
    """
    tp_set_button 함수는 tp 객체의 모든 요소에 대해 지정된 port와 btn의 상태[켜짐|꺼짐] 를 설정합니다.
    """
    for t in tp:
        if t:
            t.port[port].channel[btn].value = state
# ---------------------------------------------------------------------------- #
def tp_send_level(tp, port, lvl, value):
    """
    tp_send_level 함수는 tp 객체의 모든 요소에 대해 지정된 port와 lvl에 value를 전송합니다.
    """
    for t in tp:
        if t:
            t.port[port].level[lvl].value = value
# ---------------------------------------------------------------------------- #
def convert_text_to_unicode(text):
    """
    convert_text_to_unicode 함수는 주어진 텍스트를 유니코드 아스키로 변환하여 반환합니다.
    """
    return "".join(format(ord(char), "04X") for char in text)
# ---------------------------------------------------------------------------- #
def tp_set_btn_text_unicode(tp, port, addr, text):
    """
    tp_set_btn_text_unicode 함수는 tp 객체의 모든 요소에 대해 지정된 port, addr, text를 이용하여 버튼에 유니코드 텍스트를 표시합니다.
    """
    tp_send_command(tp, port, addr, f"^UNI-{addr},0," + convert_text_to_unicode(text))
# ---------------------------------------------------------------------------- #
def tp_set_btn_text(tp, port, addr, text):
    """
    tp_set_btn_text 함수는 tp 객체의 모든 요소에 대해 지정된 port, addr, text를 이용하여 버튼에 텍스트를 표시합니다.
    """
    tp_send_command(tp, port, addr, f"^TXT-{addr},0," + text)
# ---------------------------------------------------------------------------- #
