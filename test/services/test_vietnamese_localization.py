"""Kiểm tra bản Việt hóa, chạy bằng thư viện chuẩn, không cần khóa API."""
import ast
import json
from pathlib import Path
import string
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[2]


class VietnameseLocalizationTest(unittest.TestCase):
    def setUp(self):
        self.en = json.loads((ROOT / 'webui/i18n/en.json').read_text())['Translation']
        self.vi = json.loads((ROOT / 'webui/i18n/vi.json').read_text())['Translation']

    def test_complete_nonempty_catalog(self):
        self.assertFalse(set(self.en) - set(self.vi))
        for key in self.en:
            with self.subTest(key=key):
                self.assertTrue(self.vi[key].strip())

    def test_format_fields_preserved(self):
        def fields(value):
            return sorted((field, spec, conversion) for _, field, spec, conversion
                          in string.Formatter().parse(value) if field is not None)
        for key, value in self.en.items():
            with self.subTest(key=key):
                self.assertEqual(fields(value), fields(self.vi[key]))

    def test_valid_config_and_vietnamese_font(self):
        config = tomllib.loads((ROOT / 'config.example.toml').read_text())
        self.assertEqual(config['ui']['language'], 'vi')
        self.assertEqual(config['ui']['video_language'], 'vi-VN')
        self.assertTrue(config['ui']['voice_name'].startswith('vi-VN-'))
        self.assertTrue((ROOT / 'resource/fonts' / config['ui']['font_name']).is_file())
        self.assertEqual(config['app']['api_key'], '')

    def test_provider_tips_allow_vietnamese(self):
        tree = ast.parse((ROOT / 'webui/Main.py').read_text())
        functions = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
        for name in ('get_llm_provider_tips', 'get_tts_provider_tips'):
            sets = [node for node in ast.walk(functions[name]) if isinstance(node, ast.Set)]
            self.assertTrue(any({'zh', 'en', 'vi'} <= {item.value for item in node.elts
                                if isinstance(item, ast.Constant)} for node in sets))

    def test_saved_language_still_has_priority(self):
        tree = ast.parse((ROOT / 'app/utils/utils.py').read_text())
        function = next(n for n in tree.body if isinstance(n, ast.FunctionDef)
                        and n.name == 'resolve_ui_language')
        namespace = {'Iterable': list}
        exec(compile(ast.Module(body=[function], type_ignores=[]), '<language>', 'exec'), namespace)
        resolve = namespace['resolve_ui_language']
        self.assertEqual(resolve('vi', 'en-US', ['en', 'vi']), 'vi')
        self.assertEqual(resolve('en', 'vi-VN', ['en', 'vi']), 'en')


if __name__ == '__main__':
    unittest.main()
