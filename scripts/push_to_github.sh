#!/usr/bin/env bash
# ==============================================================================
# Motion Craft - Push to GitHub Helper
# ==============================================================================

set -e

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_DIR"

echo "=========================================================="
echo "🎬 Motion Craft - GitHub Remote Publisher"
echo "=========================================================="

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "• Inisialisasi Git repository..."
    git init -b main
fi

# Ensure all files are tracked
git add .
if ! git diff --cached --quiet; then
    git commit -m "feat: initial commit - programmatic motion graphics engine"
fi

# Check remote
CURRENT_REMOTE=$(git remote get-url origin 2>/dev/null || true)

if [ -n "$CURRENT_REMOTE" ]; then
    echo "• Remote origin sudah terpasang: $CURRENT_REMOTE"
    read -p "Apakah Anda ingin langsung push ke origin ini? (y/n): " CONFIRM
    if [[ "$CONFIRM" =~ ^[Yy]$ ]]; then
        git push -u origin main
        echo "✅ Berhasil di-push ke $CURRENT_REMOTE"
    fi
else
    echo ""
    echo "📌 Remote origin belum terpasang."
    echo "Langkah membuat repo di GitHub:"
    echo "1. Buka https://github.com/new"
    echo "2. Beri nama repo (misal: 'motion-craft' atau 'motion-graphics-engine')"
    echo "3. Pilih Public / Private (jangan centang Add README)"
    echo "4. Salin URL repositori Anda (misal: https://github.com/<username>/motion-craft.git)"
    echo ""
    read -p "Masukkan GitHub Repo URL Anda: " REPO_URL

    if [ -n "$REPO_URL" ]; then
        git remote add origin "$REPO_URL"
        echo "• Menghubungkan ke origin..."
        git push -u origin main
        echo "✅ Repositori berhasil dipublish ke GitHub: $REPO_URL"
    else
        echo "⚠️ Dibatalkan. Anda dapat menjalankannya nanti dengan: bash scripts/push_to_github.sh"
    fi
fi
