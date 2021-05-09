import sys
import subprocess as ps


def test_render(file_to_render, class_to_render):
    print('Rendering test file in 720p @ 60 fps')
    ps.call([
        'manim', '-p', '-ql', file_to_render, class_to_render
    ], shell=True)


def full_hd_render(file_to_render, class_to_render):
    print('Rendering file in 1080p @ 60 fps')
    ps.call([
        'manim', file_to_render, class_to_render], shell=True)


def render(_, render_type, file_to_render, class_to_render):
    if render_type == 'test':
        test_render(file_to_render, class_to_render)
    else:
        full_hd_render(file_to_render, class_to_render)


if __name__ == '__main__':
    render(*sys.argv)
